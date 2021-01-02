#!/usr/bin/env python3
from flask import redirect

redirect_to_url = "https://www.applevalleyhockey.com/avhsboys"


def main(request):
    return redirect(redirect_to_url, code=301)