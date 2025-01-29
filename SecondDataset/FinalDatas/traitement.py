import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_graphs_for_csv_files(folder_path):
    """Créer des graphiques pour chaque colonne sauf la première dans les fichiers CSV d'un dossier."""
    # Lister tous les fichiers CSV dans le dossier
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".csv"):  # Protection contre la casse des extensions
            file_path = os.path.join(folder_path, filename)
            
            try:
                # Lire le fichier CSV
                df = pd.read_csv(file_path)
                
                # Remplacer les '/' par des underscores dans les colonnes
                df.columns = df.columns.str.replace('/', '_')
                
                # Pour chaque colonne sauf la première, créer un graphique
                for column in df.columns[1:]:
                    plt.figure(figsize=(10, 6))
                    
                    # Tracer les données de chaque CSV
                    for csv_file in os.listdir(folder_path):
                        if csv_file.lower().endswith(".csv"):  # Protection contre la casse des extensions
                            file_path = os.path.join(folder_path, csv_file)
                            try:
                                df = pd.read_csv(file_path)
                                # Remplacer les '/' par des underscores dans les colonnes
                                df.columns = df.columns.str.replace('/', '_')
                                
                                # Tracer la colonne de données
                                plt.plot(df.iloc[:, 0], df[column], label=csv_file)
                            except Exception as e:
                                print(f"Erreur lors de la lecture du fichier {csv_file}: {e}")
                    
                    # Ajouter des labels, une légende, et définir les limites des axes
                    plt.xlabel(df.columns[0])  # Utilise la première colonne comme abscisse
                    plt.ylabel(column)  # Utilise le nom de la colonne comme ordonnée
                    plt.title(f"Graphique de la colonne {column}")
                    plt.legend()
                    
                    # Définir les limites des axes des ordonnées (entre 0 et 2)
                    plt.ylim(0, 1)
                    
                    # Sauvegarder le graphique dans le dossier avec un nom valide
                    output_path = os.path.join(folder_path, f"{column}_graph.png")
                    plt.savefig(output_path)
                    plt.close()
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier {filename}: {e}")

# Utilisation
folder_path = 'c:\\Users\\theob\\Desktop\\AI results'  # Remplace ce chemin par le chemin réel de ton dossier
plot_graphs_for_csv_files(folder_path)
