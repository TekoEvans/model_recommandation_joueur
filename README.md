# model_recommandation_joueur

# 🧠⚽ Football Player Recommendation System

Ce projet vise à développer un système de recommandation basé sur l’analyse des performances des joueurs de football à l’aide d’un modèle de langage pré-entraîné (LLM) finement ajusté (fine-tuned) avec la méthode LoRA.

## 📌 Objectif

Fournir des recommandations personnalisées aux joueurs de football pour améliorer leur jeu, leur positionnement, ou identifier les meilleures opportunités de progression, en s’appuyant sur des statistiques de performance et l’analyse contextuelle à l’aide d’un modèle de langage léger.

## 🛠️ Technologies utilisées

- **Python 3.9.21**
- **TinyLLaMA** (modèle LLM léger)
- **LoRA** (Low-Rank Adaptation)
- **Transformers** (Hugging Face)
- **Datasets** (Hugging Face)
- **PyTorch / PEFT**
- **Pandas / NumPy**
- **Scikit-learn** (pour le prétraitement éventuel)
- **FastAPI** (pour l’API de recommandation)
- **Docker** (pour conteneuriser les services)
- **Kubernetes** (scalabilité des modules d’inférence)

## 🧬 Données

Les données sont constituées de statistiques de joueurs, telles que :
- Nombre de buts, passes décisives
- Minutes jouées
- Taux de réussite des passes
- Poste.

Les données sont prétraitées et transformées en prompts exploitables par le modèle de langage.

## 🔄 Entraînement

Le fine-tuning est réalisé avec la méthode **LoRA** afin d’adapter efficacement un modèle LLM léger (TinyLLaMA) aux spécificités des recommandations footballistiques.


