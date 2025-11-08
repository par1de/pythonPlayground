import time
import argparse
import pyautogui

def main():
    parser = argparse.ArgumentParser(
        description="Clicca il tasto sinistro del mouse ogni mezzo secondo per X secondi oppure per Y volte."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-t", "--time",
        type=float,
        help="Tempo (in secondi) per cui cliccare il tasto sinistro del mouse ogni mezzo secondo."
    )
    group.add_argument(
        "-n", "--num",
        type=int,
        help="Numero di click del tasto sinistro del mouse."
    )

    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=0.5,
        help="Intervallo tra i click (secondi). Default: 0.5"
    )

    parser.add_argument(
        "-d", "--delay",
        type=float,
        default=5,
        help="Secondi di attesa prima di iniziare (per mettere il focus sulla finestra). Default: 5"
    )

    args = parser.parse_args()

    print(f"Parto tra {args.delay} secondi... metti il focus sulla finestra giusta.")
    time.sleep(args.delay)

    if args.time is not None:
        # Modalità: premi ogni intervallo per un tempo totale X
        print(f"Premo SPACE ogni {args.interval} secondi per {args.time} secondi...")
        end_time = time.time() + args.time
        count = 0
        while time.time() < end_time:
            pyautogui.click()
            count += 1
            time.sleep(args.interval)
        print(f"Fatto. Premuto {count} volte.")
    else:
        # Modalità: premi Y volte
        print(f"Premo SPACE {args.num} volte (intervallo {args.interval}s)...")
        for _ in range(args.num):
            pyautogui.click()
            time.sleep(args.interval)
        print("Fatto.")

if __name__ == "__main__":
    main()
