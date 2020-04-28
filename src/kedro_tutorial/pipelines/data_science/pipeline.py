from kedro.pipeline import Pipeline, node

from kedro_tutorial.pipelines.data_science.nodes import (
    evaluate_model,
    split_data,
    train_model,
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=split_data,
                inputs=["master_table", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
            ),
            node(
                train_model, ["X_train", "y_train"], "regressor", tags=["my-regressor-node"],
            ),
            node(
                func=evaluate_model,
                inputs=["regressor", "X_test", "y_test"],
                outputs=None,
            ),
        ],
        tags=["ds_tag"],
    )
