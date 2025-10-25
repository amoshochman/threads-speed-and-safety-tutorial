# Threads Speed and Safety Tutorial

This repo contains small Python demos exploring threading concepts.

## Setup
Before running **io_threads_demo.py**, start a simple local HTTP server:
python3 -m http.server 8000   # or: python -m http.server 8000
(to simulate a local I/O endpoint)

## Files
- io_threads_demo.py — demonstrates race conditions, thread safety with locks, and I/O concurrency.
- cpu_parallel_demo.py — will compare threading vs multiprocessing for CPU-bound tasks (to be added).

## How to Run
Run any script directly:
python <filename>.py

These examples illustrate the difference between safe vs unsafe shared data access and the performance impact of parallelism in I/O vs CPU tasks.