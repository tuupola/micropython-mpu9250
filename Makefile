.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Available tasks:"
	@echo "    watch  Upload changed *.py files to board automatically"
	@echo "    shell  Start an remote shell session"
	@echo "    sync   Upload all *.py files to board"
	@echo "    reset  Soft reboot the board"
	@echo "    repl   Start a repl session"
	@echo "    deps   Install dependencies with upip"
	@echo ""

watch:
	find . -name "*.py" | entr -c sh -c 'make sync && make reset'

sync:
	rshell --port /dev/tty.SLAB_USBtoUART --timing --buffer-size=32 cp --recursive *.py /flash

shell:
	rshell --port /dev/tty.SLAB_USBtoUART --timing --buffer-size=32

repl:
	screen /dev/tty.SLAB_USBtoUART 115200

reset:
	rshell --port /dev/tty.SLAB_USBtoUART --timing --buffer-size=32 repl "~ import machine ~ machine.reset()~"

dist:
	python3 setup.py sdist

# twine upload dist/filename.tar.gz

.PHONY: help watch shell repl reset sync dist
