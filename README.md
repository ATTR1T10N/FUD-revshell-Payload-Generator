# Payload-Generator

Payload-Generator is a tool for generating network payloads and listening to connections on remote systems. Developed for penetration testing environments, it allows creating and executing payloads from an attacker machine to a victim machine using PowerShell.

## Features

- Customized payload generation
- Real-time connection listening
- Intuitive command-line interface
- Automated execution of `netcat` to listen for connections

## Screenshots

**Payload Generator**

![Inicio de Payload-Generator](https://github.com/ccyl13/Payload-Generator/blob/main/Payload%20Generator.png?raw=true)


## Dependencies

The tool is developed in Python 3 and requires the following dependencies:
- `colorama` for command-line interface colors
- `netcat` to listen for network connections on the attacker machine

Installation:

```bash
pip3 install colorama
git clone https://github.com/ATTR1T10N/FUD-revshell-Payload-Generator.git
cd Payload-Generator
chmod +x payload_generator.py
python3 payload_generator.py

