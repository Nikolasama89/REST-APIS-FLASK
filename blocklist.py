"""
blocklist.py

This file just contains the blocklist of JWT tokens. It will be imported by
the app and the logout resource so that tokens can be added to the blocklist when
the user logs out.

"""
# IT IS BEST PRACTICE TO USE A DATABASE AND NOT A SET LIKE WE HAVE HERE
# BECAUSE EVERY TIME WE RERUN THE APP EVERYTHING IS DELETED
# IT IS BEST TO USE REDIS


BLOCKLIST = set()
