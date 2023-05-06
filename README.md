# DStreamer Real-Time Video Streaming Application

This is a web application that allows users to stream live video and watch live video streams from other users. It uses WebSockets and the MediaStream API to capture and transmit live video and audio data between the clients and the server.

## Features

- Start a new video stream by creating a new room with a unique code.
- Join an existing video stream by entering the room code in the URL.
- Stream live video to other users in real-time.
- Watch live video streams from other users in real-time.

## Technologies & Frameworks Used

- Python
- Django
- Django Channels
- WebSocket protocol
- JavaScript
- MediaStream API
- Tailwind CSS
- Daisy UI

## Installation

To install and run the application, follow these steps:

1. Clone the repository:

```
git clone https://github.com/notnotrachit/dstreamer.git
```

2. Navigate to the project directory:

```
cd dstreamer
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Run the development server:

```
python manage.py runserver
```

5. Open your web browser and go to http://localhost:8000

## Usage

To start a new test stream, click on "`Start stream`" on the home page. To create a new public room stream, click on "`New Public Room`" & enter a unique room code in the input field and click "`Start Stream`". This will redirect you to the new stream page, where you can start streaming live video.

To join an existing video stream, you can either go to the stream url directly or click on "`Join Room`". This will take you to the a new page where you can enter the room code & watch the live video stream.

## Limitation
Currently it only broadcasts video & not audio