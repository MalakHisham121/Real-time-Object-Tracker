# Real-time-Object-Tracker

A real-time object tracker using Computer Vision.

## Installation

You will need to install the required libraries. Run the following command:

```bash
pip install opencv-python opencv-contrib-python
```

## Under the Hood

The tracker is implemented using the **MOSSE** tracker. This algorithm is lightweight and uses older algorithms to predict the next shift for the object. It is highly speed-efficient and perfectly appropriate to run on a standard CPU.

## Usage

1. Run the file to start the camera feed.
2. Press **`s`** or **`S`** to move to the selection state.
3. Draw a bounding box to choose a specific object to be tracked. 
   > **Note:** Make sure you don't capture the background. Keep the bounding box tight to the object to get the most accurate results.
4. Press **`q`** or **`Q`** to exit the camera.