release: ./release-steps.sh
web: cd network-api && gunicorn networkapi.wsgi:application --preboot --max-requests 2000