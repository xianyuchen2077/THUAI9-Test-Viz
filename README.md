# THUAI9-Test-Viz

A visualization and testing tool for THUAI9 development logs.

## Project Overview

The repository combines backend and client code with a Python development-test workspace for:

- log and protobuf data decoding
- event-driven processing
- interactive playback and round control
- Tkinter-based visualization
- functional testing and utility conversion

The main test-development workspace is:

```text
THUAI9-Backend-master/client/client_gRPC/dev_test/
├── data/
├── core/
│   ├── decoder.py
│   └── events.py
├── ui/
│   ├── main_ui.py
│   └── components.py
├── logic/
│   └── controller.py
├── tests/
│   └── test_cases.py
├── utils/
│   └── converter.py
└── main.py
```

## My Contribution

This is a **team project**, and I contributed to only part of it rather than developing the complete system independently.

Commit [`e26a948`](https://github.com/xianyuchen2077/THUAI9-Test-Viz/commit/e26a948a0600b12c1f1be8cb04371ffcb350f7cd), authored by `xianyuchen2077`, verifies my work on:

- `ui/components.py`: reusable information and button panels, player summary cards, hover details, a responsive 20 × 20 chessboard, and a composite status panel
- `ui/main_ui.py`: the initial Tkinter window layout, player and board areas, operation controls, information display, and initialization/reset UI scaffolding

That commit is described as an initial UI layout with functionality still to be completed. The repository history does **not** verify that I implemented the decoder, controller, backend, protobuf layer, or test suite, so those modules are not claimed as my contribution.

## Running the Development Tools

The Python client requirements include `grpcio`, `grpcio-tools`, `protobuf`, `numpy`, and `colorama`. From `THUAI9-Backend-master/client/client_gRPC/`, install them with:

```bash
python -m pip install -r requirements.txt
```

The current `dev_test/main.py` starts the controller-driven test loop. The Tkinter layout can also be launched directly from its `ui/` directory:

```bash
python main_ui.py
```

## Contribution Boundary

- Confirmed: initial Tkinter UI components and layout in the two files above
- Not confirmed: backend logic, decoding, controller implementation, protobuf integration, or tests
- **TODO:** add any additional contribution only after it can be supported by another commit, review record, or course-development record
