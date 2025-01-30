import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from ultralytics import YOLO



def train_evaluate_predict(lr_values, batch_sizes):
    # Charger le modèle pré-entraîné
    base_model = YOLO('yolov8n.pt')  # Modèle Nano, adapté pour un GPU de 8 Go

    # Dossier pour sauvegarder les résultats
    results_dir = "experiment_results"
    os.makedirs(results_dir, exist_ok=True)

    # Chemin vers le fichier de données et le dossier de test
    data_path = 'C:\\Users\\theob\\Documents\\ENSC\\Ia_semestre\\Landmining_project_ENSC\\SecondDataset\\Landmines_detection_dataset_v4i_yolov8\\data.yaml'
    test_images_path = 'C:\\Users\\theob\\Documents\\ENSC\\Ia_semestre\\Landmining_project_ENSC\\SecondDataset\\Landmines_detection_dataset_v4i_yolov8\\test\\images'

    for lr in lr_values:
        for batch in batch_sizes:
            experiment_name = f"landmine_lr_{lr}_batch_{batch}_wd00001"
            print(f"\n🔍 Training with Learning Rate: {lr}, Batch Size: {batch}")

            # Étape 1 : Entraîner le modèle
            results = base_model.train(
                data=data_path,
                epochs=50,  # Vous pouvez ajuster ce nombre
                imgsz=640,
                batch=batch,
                lr0=lr,  # Appliquer le learning rate
                weight_decay=0.0001,
                name=experiment_name
            )

            # Sauvegarde des logs d'entraînement
            results_file = os.path.join(results_dir, f"{experiment_name}_training.log")
            with open(results_file, "w") as f:
                f.write(str(results))

            # Étape 2 : Évaluer le modèle
            print(f"Evaluating the model: {experiment_name}")
            metrics = base_model.val(data=data_path)

            # Sauvegarde des métriques d'évaluation
            metrics_file = os.path.join(results_dir, f"{experiment_name}_metrics.log")
            with open(metrics_file, "w") as f:
                f.write(str(metrics))

            # Étape 3 : Effectuer des prédictions
            print(f"🔎 Predicting using the model: {experiment_name}")
            predictions = base_model.predict(
                source=test_images_path,
                save=True,
                conf=0.2,
                project=os.path.join(results_dir, experiment_name),
                name="predictions"
            )

            # Sauvegarde des prédictions
            predictions_file = os.path.join(results_dir, f"{experiment_name}_predictions.log")
            with open(predictions_file, "w") as f:
                f.write(str(predictions))

if __name__ == "__main__":
    # Hyperparamètres à tester
    learning_rates = [0.01]
    batch_sizes = [16]

    # Lancer les expériences
    train_evaluate_predict(learning_rates, batch_sizes)
