"""Command-line interface for Acton."""

import logging
import sys

import acton.acton
import acton.predictors
import acton.recommenders
import click


# acton


@click.command()
@click.option('--data',
              type=click.Path(exists=True, dir_okay=False),
              help='Path to features/labels file',
              required=True)
@click.option('-l', '--label',
              type=str,
              help='Column name of labels',
              required=True)
@click.option('-o', '--output',
              type=click.Path(dir_okay=False),
              help='Path to output file',
              required=True)
@click.option('-f', '--feature',
              type=str,
              multiple=True,
              help='Column names of features')
@click.option('--epochs',
              type=int,
              help='Number of epochs to run active learning for',
              default=100)
@click.option('-i', '--id',
              type=str,
              help='Column name of IDs')
@click.option('--diversity',
              type=float,
              help='Diversity of recommendations',
              default=0.0)
@click.option('--recommendation-count',
              type=int,
              help='Number of recommendations to make',
              default=1)
@click.option('--labeller-accuracy',
              type=float,
              help='Accuracy of simulated labellers',
              default=1.0)
@click.option('--initial-count',
              type=int,
              help='Number of random instances to label initially',
              default=10)
@click.option('--predictor',
              type=click.Choice(acton.predictors.PREDICTORS.keys()),
              default='LogisticRegression',
              help='Predictor to use')
@click.option('--recommender',
              type=click.Choice(acton.recommenders.RECOMMENDERS.keys()),
              default='RandomRecommender',
              help='Recommender to use')
@click.option('--pandas-key',
              type=str,
              default='',
              help='Key for pandas HDF5')
@click.option('-v', '--verbose',
              is_flag=True,
              help='Verbose output')
def main(
        data: str,
        label: str,
        output: str,
        feature: str,
        epochs: int,
        id: str,
        diversity: float,
        recommendation_count: int,
        labeller_accuracy: float,
        initial_count: int,
        predictor: str,
        recommender: str,
        verbose: bool,
        pandas_key: str,
):
    logging.warning('Not implemented: diversity, id_col, labeller_accuracy')
    logging.captureWarnings(True)
    if verbose:
        logging.root.setLevel(logging.DEBUG)
    return acton.acton.main(
        data_path=data,
        feature_cols=feature,
        label_col=label,
        output_path=output,
        n_epochs=epochs,
        initial_count=initial_count,
        recommender=recommender,
        predictor=predictor,
        pandas_key=pandas_key,
        n_recommendations=recommendation_count)


# acton-predict


@click.command()
@click.option('--predictor',
              type=click.Choice(acton.predictors.PREDICTORS.keys()),
              default='LogisticRegression',
              help='Predictor to use')
@click.option('-v', '--verbose',
              is_flag=True,
              help='Verbose output')
def predict(
        predictor: str,
        verbose: bool,
):
    logging.captureWarnings(True)
    if verbose:
        logging.root.setLevel(logging.DEBUG)
    return acton.acton.predict(predictor=predictor)


# acton-recommend


@click.command()
@click.option('--diversity',
              type=float,
              help='Diversity of recommendations',
              default=0.0)
@click.option('--recommendation-count',
              type=int,
              help='Number of recommendations to make',
              default=1)
@click.option('--recommender',
              type=click.Choice(acton.recommenders.RECOMMENDERS.keys()),
              default='RandomRecommender',
              help='Recommender to use')
@click.option('-v', '--verbose',
              is_flag=True,
              help='Verbose output')
def recommend(
        diversity: float,
        recommendation_count: int,
        recommender: str,
        verbose: bool,
):
    logging.warning('Not implemented: diversity')
    logging.captureWarnings(True)
    if verbose:
        logging.root.setLevel(logging.DEBUG)
    return acton.acton.recommend(
        recommender=recommender,
        n_recommendations=recommendation_count)


# acton-label


@click.command()
@click.option('--data',
              type=click.Path(exists=True, dir_okay=False),
              help='Path to labels file',
              required=True)
@click.option('-l', '--label',
              type=str,
              help='Column name of labels',
              required=True)
@click.option('-f', '--feature',
              type=str,
              multiple=True,
              help='Column names of features')
@click.option('--labeller-accuracy',
              type=float,
              help='Accuracy of simulated labellers',
              default=1.0)
@click.option('--pandas-key',
              type=str,
              default='',
              help='Key for pandas HDF5')
@click.option('-v', '--verbose',
              is_flag=True,
              help='Verbose output')
def label(
        data: str,
        feature: str,
        label: str,
        labeller_accuracy: float,
        verbose: bool,
        pandas_key: str,
):
    logging.warning('Not implemented: labeller_accuracy')
    logging.captureWarnings(True)
    if verbose:
        logging.root.setLevel(logging.DEBUG)
    return acton.acton.label(
        data_path=data,
        feature_cols=feature,
        label_col=label,
        pandas_key=pandas_key)


if __name__ == '__main__':
    sys.exit(main())
