from .generate_class import Generate

class CreateAPP(Generate):
    def __init__(self):
        super().__init__()
        # BOOT    
        self.create_app()
    
    def create_app(self):
        self.generate_create_init_file('')
        self.create_main()
            
    def create_main(self):
        self.generate_create_files('', 'main.py', 'w', 'generate/files/main/generate_main.txt')
