
import uuid
from urllib.parse import unquote_plus

import boto3
import pymilvus
import face_recognition

s3_client = boto3.client(
	's3',
	endpoint_url='http://localhost:9000',
	aws_access_key_id='minioadmin',
	aws_secret_access_key='minioadmin')

pymilvus.connections.connect('default', host='localhost', port='19530')

# refer to face_recognition library
# of `face_encodings` function
FACE_ENCODING_DIMENSION=128

user_face_schema_fields = [
  	# assuming user_id datatype is uuid
  	pymilvus.FieldSchema(name='id', dtype=pymilvus.DataType.INT64, is_primary=True, auto_id=True),
  	pymilvus.FieldSchema(name='user_id', dtype=pymilvus.DataType.VARCHAR, max_length=128),
	pymilvus.FieldSchema(name='embeddings', dtype=pymilvus.DataType.FLOAT_VECTOR, dim=FACE_ENCODING_DIMENSION)]

milvus_user_face_schema = pymilvus.CollectionSchema(user_face_schema_fields, 'schema of user face')

milvus_users_faces = pymilvus.Collection('users_faces', milvus_user_face_schema)

milvus_users_faces.create_index(
	'embeddings', {
		'index_type': 'IVF_FLAT',
		'metric_type': 'L2',
		'params': {'nlist': 128}})

def face_recognize(face_encodings_to_search_for):
	''' function to search for face stored'''
	results = milvus_users_faces.search(
		face_encodings_to_search_for,
		'embeddings',
		{'metric_type': 'L2', 'params': {'nprobe': 16}},
		limit=2,
		output_fields=['user_id'])

	return results

def lambda_handler(event, _context):
	# assuming frontend already made sure
	# the image has one face within it
	for record in event['Records']:
		bucket = record['s3']['bucket']['name']
		facial_image_s3_file_path = unquote_plus(record['s3']['object']['key'])
		tmpkey = facial_image_s3_file_path.replace('/', '')
		facial_image_download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)

		# assuming user_id is end of the s3 file path key
		# and it is uuid
		user_id = tmpkey.split('.')[0]

		s3_client.download_file(bucket, facial_image_s3_file_path, facial_image_download_path)

		face_image = face_recognition.load_image_file(facial_image_download_path)
		face_locations = face_recognition.face_locations(face_image, model="hog")
		face_encodings = face_recognition.face_encodings(face_image, face_locations)

		milvus_users_faces.insert([[user_id], face_encodings])

		# manually call flush for testing
		# milvus_users_faces.flush()

# for testing locally
if __name__ == '__main__':
	import json

	user_id = '3f35928a-9ced-4147-b32c-70ca09d4a7bf'

	s3_client.upload_file(
		f'./sample-dataset/users/scarlet-johansson/{user_id}.jpg',
		'users-faces',
		user_id)

	# simulate lambda hook being called
	lambda_handler({
		'Records': [{'s3': {'bucket': {'name': 'users-faces'}, 'object': {'key': user_id}}}]}, {})

	milvus_users_faces.load()

	# face recognizer should set
	# appropriate threshold to know
	# which distance should be considered
	# as face recognized

	# should get lower distance
	# indicate that face are similar
	face_image = face_recognition.load_image_file('./sample-dataset/tests/scarlet-johansson/0.jpg')
	face_locations = face_recognition.face_locations(face_image, model="hog")
	face_encodings = face_recognition.face_encodings(face_image, face_locations)
	scarlet_johansson_face_recognize =  face_recognize(face_encodings)

	# should get higher distance
	# indicate that face not similar
	face_image = face_recognition.load_image_file('./sample-dataset/tests/hailee-steinfeld/0.webp')
	face_locations = face_recognition.face_locations(face_image, model="hog")
	face_encodings = face_recognition.face_encodings(face_image, face_locations)
	hailee_steinfeld_face_recognize =  face_recognize(face_encodings)

	pymilvus.utility.drop_collection('users_faces')
