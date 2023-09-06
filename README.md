<h2> Bitcoin Price Tracker </h2>

<h3> Introduction </h3>

Ce dépôt contient un script Python (`bitcoin_tracker.py`) pour suivre et visualiser les données de prix du Bitcoin. Il utilise l'API CoinGecko pour récupérer des données de prix historiques et offre des fonctionnalités de personnalisation et de tracé.

<h3> Caractéristiques </h3>

   - Récupération des données de prix: Récupérez les données historiques de prix du Bitcoin dans la devise de votre choix.

   - Personnalisable: Personnalisez la cryptomonnaie, la devise et le nombre de jours de données historiques.

   - Graphe: Tracez les données de prix historiques du Bitcoin avec une moyenne mobile de 30 jours.

   - Gestion des erreurs: Gérez les échecs de demande API et les réponses non valides.

<h3> Prérequis: </h3>

   - Python3 installé sur votre système.
  
   - Packages Python requis installés (`requests`, `numpy`, `matplotlib`, `termcolor`, `pycoingecko`).

<h3> Utilisation: </h3>

   - Utilisez ce script pour suivre et analyser les données sur les prix de Bitcoin.

   - Personnalisez-le pour vos projets d'analyse de crypto-monnaie.

   - Étendez-le avec des fonctionnalités et des indicateurs supplémentaires.

Clonez le dépôt: 

```bash
git clone https://github.com/Ferrerkomi/bitcoin_tracker.git 
```

Accédez au dossier du dépôt: 

```bash
cd bitcoin_tracker
``` 

Installez les packages Python requis: 

```bash
pip install requests numpy matplotlib termcolor pycoingecko
```

Ouvrez 'bitcoin_tracker.py' et personnalisez la cryptomonnaie, la devise et le nombre de jours selon vos besoins (Bitcoin par défaut).

   - Modifiez la crypto-monnaie, la devise et la plage de données dans la fonction `main`.

   - Spécifiez une police personnalisée en fournissant le chemin du fichier de police.


Exécutez le script: 

```bash
python3 bitcoin_tracker.py
```

Le script récupérera les données de prix du Bitcoin, les tracera et affichera le graphique dans python launcher.

<h3> Extension et Contribution: </h3>

N'hésitez pas à étendre ce script pour suivre d'autres cryptomonnaies ou implémenter des analyses plus avancées. Les contributions et les améliorations sont les bienvenues.


<h3> Remerciements: </h3>

  **_API CoinGecko_**

  **_BitcoinUtils_**

  **_Matplotlib_**
