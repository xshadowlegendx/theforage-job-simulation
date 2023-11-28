package com.example.theforage.standardbank.task0

import java.time.LocalDate
import java.time.ZoneOffset

import com.nimbusds.jose.jwk.JWK
import com.nimbusds.jwt.SignedJWT
import com.nimbusds.jose.JWSHeader
import com.nimbusds.jwt.JWTClaimsSet
import com.nimbusds.jose.JWSAlgorithm
import com.nimbusds.jose.jwk.OctetKeyPair
import com.nimbusds.jose.crypto.Ed25519Signer
import com.nimbusds.jose.crypto.Ed25519Verifier
import org.springframework.http.HttpStatus
import org.springframework.core.io.Resource
import org.springframework.http.ResponseEntity
import org.springframework.stereotype.Controller
import org.springframework.beans.factory.annotation.Value
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.ResponseBody
import org.springframework.web.bind.annotation.RequestHeader
import org.springframework.security.crypto.argon2.Argon2PasswordEncoder

import com.nimbusds.jose.jwk.Curve
import com.nimbusds.jose.jwk.gen.OctetKeyPairGenerator

@Controller
class SimpleJwtDemoController(@Value("\${jwtPrivateSigningKey}") private val jwtPrivateSigningKeyResource: Resource) {
    private val argon2 = Argon2PasswordEncoder(16, 32, 1, 60000, 10)

    private val jwtSigner: Ed25519Signer

    private val jwtVerifier: Ed25519Verifier

    private val signingKey: JWK

    // jean password, abc123
    private val users = mapOf<String, Map<String, String>>(
        "jean" to mapOf("id" to "48cd0bffb4e041dab2adaafac52d0756", "username" to "jean", "password" to "\$argon2id\$v=19\$m=60000,t=10,p=1\$UHTatFoGbymzcI6t0piLXQ\$iSgavQUC+4xvez7R2N2uFOiVEOlMikdQjZk5gG9zCC0"))

    init {
        // nimbus cannot parse ed25519 private key for now
        // val jwtPrivateSigningKey = this.jwtPrivateSigningKeyResource.inputStream.bufferedReader().use { it.readText() }

        this.signingKey = OctetKeyPairGenerator(Curve.Ed25519).keyID("admin@example.com").generate()

        this.jwtVerifier = Ed25519Verifier(this.signingKey.toPublicJWK())

        this.jwtSigner = Ed25519Signer(this.signingKey)
    }

    @GetMapping("/protected")
    @ResponseBody
    fun protected(@RequestHeader("authorization") authHeader: String): ResponseEntity<*> {
        if (authHeader.isNotEmpty()) {
            val jwt = authHeader.replace("Bearer ", "")

            val signed = SignedJWT.parse(jwt)

            if (signed.verify(this.jwtVerifier)) {
                return ResponseEntity.ok("got into protected resource")
            }
        }

        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build<String>()
    }

    @GetMapping("/public")
    @ResponseBody
    fun publicResource(): String {
        return "public resource"
    }

    @PostMapping(path = ["/login"])
    @ResponseBody
    fun login(@RequestBody loginReq: LoginReqDto): ResponseEntity<*> {
        if (this.users.containsKey(loginReq.username) && this.argon2.matches(loginReq.password, this.users.get(loginReq.username)!!.get("password"))) {
            val claims = JWTClaimsSet.Builder()
                .subject(this.users.get(loginReq.username)!!.get("id"))
                .issuer("https://standardbank.theforage.example.com")
                .build();

            val signed = SignedJWT(JWSHeader.Builder(JWSAlgorithm.EdDSA).keyID(this.signingKey.keyID).build(), claims)

            signed.sign(this.jwtSigner)

            return ResponseEntity.ok(signed.serialize())
        }

        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build<String>()
    }
}
