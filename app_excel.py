import pandas as pd
import os
from uuid import uuid4

# Function to load and list sheets in an Excel file


def load_excel_file(file_path):
    """
    Loads an Excel file and returns a dictionary of DataFrames for each sheet.
    Args:
        file_path (str): Path to the Excel file.
    Returns:
        dict: Dictionary with sheet names as keys and DataFrames as values, or None if an error occurs.
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
            return None

        # Check if file has valid Excel extension
        if not file_path.lower().endswith(('.xlsx', '.xls')):
            print("Erro: O arquivo deve ter extensão .xlsx ou .xls.")
            return None

        # Load all sheets into a dictionary of DataFrames
        excel_data = pd.read_excel(file_path, sheet_name=None)
        print("\nAbas encontradas:", list(excel_data.keys()))
        return excel_data

    except Exception as e:
        print(f"Erro ao carregar o arquivo: {str(e)}")
        return None

# Function to select a sheet for processing


def select_sheet(excel_data):
    """
    Prompts the user to select a sheet from the available sheets.
    Args:
        excel_data (dict): Dictionary of sheet names and DataFrames.
    Returns:
        tuple: Selected sheet name and its DataFrame, or (None, None) if invalid.
    """
    while True:
        sheet_name = input(
            "\nSelecione a aba para processar (digite o nome): ").strip()
        if sheet_name in excel_data:
            return sheet_name, excel_data[sheet_name]
        else:
            print(f"Erro: A aba '{sheet_name}' não existe. Tente novamente.")

# Function to choose duplicate detection method


def choose_duplicate_method():
    """
    Prompts the user to choose how duplicates are detected.
    Returns:
        str: 'columns' for specific columns or 'full_row' for entire row.
    """
    while True:
        print("\nComo deseja verificar duplicatas/similares?")
        print("1. Em colunas específicas")
        print("2. Na linha completa")
        choice = input("Digite sua escolha (1 ou 2): ").strip()
        if choice == '1':
            return 'columns'
        elif choice == '2':
            return 'full_row'
        else:
            print("Erro: Escolha 1 ou 2.")

# Function to select columns for duplicate checking


def select_columns(df):
    """
    Prompts the user to select columns for duplicate detection.
    Args:
        df (pd.DataFrame): DataFrame of the selected sheet.
    Returns:
        list: List of valid column names.
    """
    print("\nColunas disponíveis:", list(df.columns))
    while True:
        columns = input(
            "Digite os nomes das colunas (separados por vírgula) para verificar duplicidade: ").strip()
        column_list = [col.strip() for col in columns.split(',')]
        invalid_cols = [col for col in column_list if col not in df.columns]
        if invalid_cols:
            print(
                f"Erro: As seguintes colunas são inválidas: {invalid_cols}. Tente novamente.")
        else:
            return column_list

# Function to identify duplicates


def identify_duplicates(df, method, columns=None):
    """
    Identifies duplicate rows based on the specified method.
    Args:
        df (pd.DataFrame): DataFrame to check for duplicates.
        method (str): 'columns' or 'full_row' to define duplicate detection.
        columns (list, optional): List of columns to check for duplicates.
    Returns:
        pd.DataFrame: DataFrame of duplicate rows with their indices.
    """
    if method == 'columns':
        duplicates = df[df.duplicated(subset=columns, keep=False)].copy()
    else:  # full_row
        duplicates = df[df.duplicated(keep=False)].copy()

    if not duplicates.empty:
        # Excel rows start at 1, +1 for header
        duplicates['Row'] = duplicates.index + 2
    return duplicates

# Function to display duplicates


def display_duplicates(duplicates, sheet_name, columns=None):
    """
    Displays duplicate rows to the user.
    Args:
        duplicates (pd.DataFrame): DataFrame containing duplicate rows.
        sheet_name (str): Name of the sheet being processed.
        columns (list, optional): Columns used for duplicate detection.
    """
    if duplicates.empty:
        print(f"\nNenhuma duplicata encontrada na aba '{sheet_name}'.")
        return

    print(f"\nDuplicatas/Similares encontradas na aba '{sheet_name}'" +
          (f" (colunas: {', '.join(columns)}):" if columns else ":"))

    for idx, row in duplicates.iterrows():
        row_data = ', '.join(f"{col}: '{row[col]}'" for col in (
            columns if columns else row.index[:-1]))
        # Find the first occurrence of this duplicate
        if columns:
            first_occurrence = df[df[columns].eq(
                row[columns]).all(axis=1)].index[0] + 2
        else:
            first_occurrence = df[df.eq(row[:-1]).all(axis=1)].index[0] + 2
        print(
            f"- Linha {row['Row']}: {row_data} (duplicata da linha {first_occurrence})")

# Function to handle duplicate removal


def remove_duplicates(df, keep='first'):
    """
    Removes duplicates from the DataFrame.
    Args:
        df (pd.DataFrame): Original DataFrame.
        keep (str): 'first' or 'last' to specify which duplicate to keep.
    Returns:
        pd.DataFrame: DataFrame with duplicates removed.
    """
    return df.drop_duplicates(keep=keep)

# Function to save the processed DataFrame


def save_processed_file(df, original_path, sheet_name):
    """
    Saves the processed DataFrame to a new Excel file.
    Args:
        df (pd.DataFrame): Processed DataFrame.
        original_path (str): Path of the original file.
        sheet_name (str): Name of the processed sheet.
    Returns:
        str: Path of the saved file, or None if an error occurs.
    """
    default_name = os.path.splitext(original_path)[0] + '_sem_duplicatas.xlsx'
    output_name = input(
        f"\nDigite o nome para o novo arquivo Excel (ex: {os.path.basename(default_name)}): ").strip()
    if not output_name:
        output_name = default_name
    elif not output_name.lower().endswith('.xlsx'):
        output_name += '.xlsx'

    try:
        df.to_excel(output_name, sheet_name=sheet_name, index=False)
        print(f"\nArquivo '{output_name}' gerado com sucesso!")
        return output_name
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {str(e)}")
        return None

# Main function to orchestrate the workflow


def main():
    global df  # For access in display_duplicates
    # Step 1: Load Excel file
    file_path = input("Digite o caminho completo do arquivo Excel: ").strip()
    excel_data = load_excel_file(file_path)
    if excel_data is None:
        return

    # Step 2: Select sheet
    sheet_name, df = select_sheet(excel_data)

    # Step 3: Choose duplicate detection method
    method = choose_duplicate_method()
    columns = None
    if method == 'columns':
        columns = select_columns(df)

    # Step 4: Identify and display duplicates
    duplicates = identify_duplicates(df, method, columns)
    display_duplicates(duplicates, sheet_name, columns)

    # Step 5: Decide action on duplicates
    if duplicates.empty:
        print("Nenhuma ação necessária, pois não há duplicatas.")
        return

    action = input(
        "\nDeseja remover as duplicatas/similares? (s/n): ").strip().lower()
    if action != 's':
        print("Mantendo todas as ocorrências. Processo finalizado.")
        return

    # Step 6: Choose which duplicate to keep
    keep = input(
        "Deseja manter a primeira ou a última ocorrência? (primeira/ultima): ").strip().lower()
    if keep not in ['primeira', 'ultima']:
        print("Erro: Escolha 'primeira' ou 'ultima'. Usando 'primeira' como padrão.")
        keep = 'primeira'
    keep = 'first' if keep == 'primeira' else 'last'

    # Step 7: Remove duplicates and save
    processed_df = remove_duplicates(df, keep)
    save_processed_file(processed_df, file_path, sheet_name)


if __name__ == "__main__":
    main()
