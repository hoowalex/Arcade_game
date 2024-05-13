class RecordManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.record = cls._instance.load_record()
        return cls._instance

    def load_record(self):
        try:
            with open("record.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_record(self):
        with open("record.txt", "w") as file:
            file.write(str(self.record))

    def update_record(self, new_record):
        if new_record > self.record:
            self.record = new_record
            self.save_record()  


record_manager = RecordManager()