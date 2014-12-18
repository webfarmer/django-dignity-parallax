
ENV_HOSTNAMES = {
    "127.0.0.1":                   "bksa.tottagency.com",
    "tottagency.co.za":            "www.tottagency.com",
    "bksa.tottagency.com":         "bksa.tottagency.com",
    "demo.tottagency.com":         "demo.tottagency.com",
}

ALLOWED_HOSTS = []

for env in ENV_HOSTNAMES:
    ALLOWED_HOSTS += ["%s" % env]

    if ENV_HOSTNAMES[env] not in ALLOWED_HOSTS:
        ALLOWED_HOSTS += ["%s" % ENV_HOSTNAMES[env]]
