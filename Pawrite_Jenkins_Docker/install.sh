rm -rf playwright_venv ||true; python3 -m virtualenv playwright_venv || true; \
	. playwright_venv/bin/activate \
	&& pip3 install -e . \
	&& pip3 install -e src/ \
	&& python3 -m playwright install
