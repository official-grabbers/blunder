# Bunder

**Short temporary Overview** : Blunder is a web application that allows users to aggregate reels and posts from multiple Instagram pages and publish them to a new page within the application. With Blunder, users can easily curate and share content from their favorite Instagram creators, all in one place. From fashion to food, travel to fitness, Blunder brings the best of Instagram to your fingertips, making it easier than ever to discover and engage with trending content. Whether you're a social media enthusiast, influencer, or content creator, Blunder empowers you to create, share, and connect like never before.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [License](#license)

## Requirements

- Docker (>=25.0.3)

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:official-grabbers/blunder.git
    ```

1. Navigate to the project directory:

    ```bash
    cd blunder
    ```

## Running the Project

1. To build the project on your machine

    ```
    docker-compose build
    ```

2. To run the project on your machine

    ```
    docker-compose up -d
    ```

The development server will be running at http://localhost:8000/ or http://127.0.0.1:8000/.

## License
- [GNU](https://github.com/official-grabbers/blunder/blob/main/LICENSE)