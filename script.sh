if [ "${PRODUCTION}" = "false" ]; then
	uvicorn main:app --host ${SERVER_HOST} --port ${SERVER_PORT} --reload
else
	uvicorn main:app --host ${SERVER_HOST} --port ${SERVER_PORT}
fi