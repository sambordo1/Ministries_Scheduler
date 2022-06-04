#!/bin/bash

mkdir -p scheduler_backend/templates
mkdir -p scheduler_backend/static
cp build-scheduler_frontend-WebAssembly*/appscheduler_frontend.html scheduler_backend/templates
cp build-scheduler_frontend-WebAssembly*/appscheduler_frontend.{js,wasm} scheduler_backend/static
cp build-scheduler_frontend-WebAssembly*/qtloader.js scheduler_backend/static
cp build-scheduler_frontend-WebAssembly*/qtlogo.svg scheduler_backend/static

