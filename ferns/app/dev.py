from ferns.app import Config, create_app

if __name__ == "__main__":
    config = Config()
    app = create_app(config)

    app.run()