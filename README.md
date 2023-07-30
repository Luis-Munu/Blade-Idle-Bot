# Blade Idle Bot

Blade Idle Bot is a project aimed at automating the process of scanning the market in the game "Blade Idle" to find valuable figures based on custom filters set by the user. This bot is designed to work specifically with the Bluestacks emulator using the standard window size and can work in the background.

Please note that this project is currently unfinished and under active development. Feel free to contribute and help improve the bot to make it more efficient and user-friendly.

## Features

- Market Scanner: The bot can automatically scan the in-game market for figures that meet the user-defined criteria by using OCR.
- Custom Filters: Users can create their own filters based on various attributes, such as rarity, level, stats, etc.
- Bluestacks Compatibility: The bot is designed to work seamlessly with the Bluestacks emulator using the standard window size.
- Auto unstuck: If an error triggers, the bot will try to setup the game to work again.

## Installation

- Clone the repository: ```git clone https://github.com/Valkam-Git/Blade-Idle-Bot.git```
- Install the required dependencies: ```pip install -r requirements.txt```

## Usage

1. Launch the Bluestacks emulator with the standard window size.
2. Open the "Blade Idle" game within the emulator and open the market tab.
3. Open a CMD window on the folder and run the bot: ```python sniper.py```
4. The bot will start scanning the market based on your custom filters.

## Configuration

You can configure the bot by editing the figures.json file. In this file, you can set up the filter criteria, including:

- Type and rarity of the figure
- Type and rarity of the stats of the figure
- Slots of the figure
- Price cap

## TODO

- Currently, the bot is spamming searches on each rarity and checking the results instead of actively filtering them, the select options mode must be finished.
- The slot recognition is not working properly, the checks always return 0-2.
- GUI.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

- Fork the repository
- Create a new branch: ```git checkout -b feature-new-feature```
- Make your changes and ```commit them: git commit -m "Add new feature"```
- Push to the branch: ```git push origin feature-new-feature```
- Submit a pull request
- Please ensure your code follows the project's coding conventions and includes appropriate tests.

**Disclaimer**
This project is intended for educational and research purposes only. Use of bots or automation in games may violate the game's terms of service and result in penalties or bans. The developers and contributors of this project are not responsible for any consequences that may arise from using this bot in the game.
