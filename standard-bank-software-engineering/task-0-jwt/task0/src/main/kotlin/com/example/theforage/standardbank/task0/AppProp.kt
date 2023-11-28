package com.example.theforage.standardbank.task0

import org.springframework.stereotype.Component
import org.springframework.beans.factory.annotation.Value

@Component
class AppProp {
    @Value("\${jwtPrivateSigningKey}")
    lateinit var jwtPrivateSigningKey: String
}
