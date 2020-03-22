.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Available tasks:"
	@echo "    watch  Upload changed library files to board automagically"
	@echo "    sync   Upload library files to board"
	@echo "    reset  Soft reboot the board"
	@echo "    repl   Start a repl session"
	@echo "    deps   Install dependencies with upip"
	@echo ""

watch:
	find . -name "*.py" | entr -c sh -c 'make sync && make reset'

sync:
	ampy --port /dev/tty.SLAB_USBtoUART put mpu6500.py
	ampy --port /dev/tty.SLAB_USBtoUART put mpu9250.py
	ampy --port /dev/tty.SLAB_USBtoUART put ak8963.py

repl:
	screen /dev/tty.SLAB_USBtoUART 115200

reset:
	ampy --port /dev/cu.SLAB_USBtoUART reset

dist:
	python3 setup.py sdist
	# twine upload dist/filename.tar.gz

.PHONY: help watch shell repl reset sync dist
