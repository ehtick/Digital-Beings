import { Twilio, twiml } from 'twilio'
import express = require('express');
import { urlencoded, Response } from 'express';
import { MessagingRequest } from './types/request';
import { message } from './routes/messages';

const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const twilioNumber = process.env.TWILIO_PHONE_NUMBER;
const twilioPort = process.env.TWILIO_PORT

let client: Twilio = undefined

export const createTwilioClient = (messageResponseHandler) => {
    console.log('init')
    if (!accountSid || !authToken || !twilioNumber)  return console.warn("No API token for Twilio bot, skipping");
    console.log('twilio client created')

}

export function sendMessage(toNumber, body) {
    client.messages.create({from: twilioNumber,
        to: toNumber,
        body: body
    }).then((message) => console.log('sent message: ' + message.sid))
    console.log('send message to: ' + toNumber + ' body: ' + body)
}