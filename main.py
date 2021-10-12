from core.apl import threads

if __name__ == '__main__':

    print("=" * 16 + " SENTINEL RUNNING " + "=" * 16)
    for t in threads:
        t.start()
  