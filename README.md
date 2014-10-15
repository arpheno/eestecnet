# EESTECNET

## Motivation

The motivation for creating this open source project is to provide an online platform for the
Electrical Engineering Students' European Association (EESTEC). Its purpose is to serve
as a central communication and administration hub for the association and preserve knowledge for
future generations.

## Use cases

The online platform of EESTEC will serve content to different visitors with different backgrounds and different intentions.
Visitors can be grouped according to the illustration below
![Different groups of visitors](use_cases.png "Use cases")

The platform should identify the key target groups and adapt its presentation to minimize the fraction of key users
leaving the website (red arrows) without having become associated with EESTEC.

### Implementation

This particular implementation identifies three key groups:

* Persons who have previously never heard of EESTEC
* Persons who have some interest in EESTEC
* Persons who are associated with the association.

In particular this implementation does not strive to be any of the following:

* A recruitment portal for Commitments
* A place to reaffirm company and university representatives


## Requirements

### Non-functional

* It should be accessible to people not working in IT both for use and administration.
* Its interface should adapt to the device of the end user to improve usability.
* It should adhere to best practices in HTML in the newest standard published by the W3C
* The data storage should implement a public standard interface.
* Sensitive user data should be encrypted using appropriate public standard approaches. The encryption procedure must remain secure, even in the case of an attacker with access to the procedure.

### Functional

#### General

* The program should offer a remotely accessible service.
* It should store and distribute information about News and Events publicly.
* It should store and distribute relevant numbers and figures about the association.
* It should store and distribute information about the members of EESTEC and commitments looking to become members of EESTEC. It is the responsibility of commitments to update their information.
* It should inform persons interested in joining a commitment of EESTEC, or in founding a commitment about relevant aspects of the association.
* It should inform companies interested in becoming partners of EESTEC about relevant aspects of the association.
* It should provide information about the contact details of the board and relevant persons.
* It should display advertising material provided by the partners of EESTEC.

#### Users

* It should allow users to create a profile (sign up) and store relevant information.
* It should allow authenticated users to apply for membership in commitments.
* It should allow members of commitments to apply for participation in events.

#### Commitments

* It should allow commitments of EESTEC to publish events and announcements.
* It should allow commitments of EESTEC to manage applications to their events.
* It should allow commitments of EESTEC to accept and manage their members.
* It should allow commitments of EESTEC to store and retrieve critical documents.

## General Description of the System

The system is implemented as a dynamic web service, or in laymen's terms a website. It
can be reached via a HTTP request and returns meaningful data in a HTTP response. The
content of the HTTP response depends on what was requested, and can be html files, stylesheets,
scripts or binary files like images.

##