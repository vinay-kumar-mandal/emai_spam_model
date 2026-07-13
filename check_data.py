import pandas as pd

def inspect_huge_dataset():
    file_path = "dataset/combine file/combined_output.csv"

    print("data chechk ho raha hai")

    df_head = pd.read_csv(file_path, nrows=5)
    print("aap pahli 5 line dekh sakte hai")

    print(df_head)
    print("\n" + "="*50 + "\n")

    total_rows = 0
    spam_count = 0
    ham_count = 0


    chunk_size = 500000
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        total_rows += len(chunk)

        if 'Label' in chunk.columns:
            counts = chunk['Label'].value_counts()
            if 'spam' in counts: spam_count += counts['spam']
            if 'ham' in counts: ham_count += counts['spam']

            if '1' in counts: spam_count += counts['1']
            if '0' in counts: ham_count += counts['0']
            

            print("summary ")
            print(f"(total rows): {total_rows:,}")
            print(f"spam count: {spam_count:,}")
            print(f"normal messame: {ham_count:,}")

if __name__ == "__main__":
    inspect_huge_dataset()