# trial1.py
import arena

def main():
    a = arena.Arena() #background_image = 'twoDots.png')
    a.add_key_car(running = True, tracer_down = True, show_rect = True)
    a.run_main_loop()

if __name__ == '__main__':
    main()
