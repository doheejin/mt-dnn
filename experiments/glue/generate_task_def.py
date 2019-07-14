from experiments.glue.glue_label_map import TaskType, DATA_TYPE, GLOBAL_MAP, TASK_TYPE, DATA_META
from data_utils.glue_utils import DataFormat

task_def_dic = {}
for task in TASK_TYPE.keys():
    task_type = TASK_TYPE[task]
    if task == "qnnli":
        task_type = TaskType.Ranking
    elif task_type == 0:
        task_type = TaskType.Classification
    elif task_type == 1:
        task_type = TaskType.Regression
    else:
        raise ValueError(task_type)

    data_format = DATA_TYPE[task]
    if task == "qnnli":
        data_format = DataFormat.PremiseAndMultiHypothesis
    elif data_format == 0:
        data_format = DataFormat.PremiseAndOneHypothesis
    elif data_format == 1:
        data_format = DataFormat.PremiseOnly
    else:
        raise ValueError(data_format)

    labels = None
    if task in GLOBAL_MAP:
        labels = GLOBAL_MAP[task].get_vocab_list()

    split_names = None
    if task == "mnli":
        split_names = ["train", "matched_dev", "mismatched_dev", "matched_test", "mismatched_test"]

    n_class = DATA_META[task]

    task_def = {"task_type": task_type.name,
                "data_format": data_format.name,
                "n_class": n_class}
    if labels is not None:
        task_def["labels"] = labels
    if split_names is not None:
        task_def["split_names"] = split_names

    if task not in ["diag", "qnnli"]:
        task_def_dic[task] = task_def

import yaml

yaml.safe_dump(task_def_dic, open("experiments/glue/glue_task_def.yml", "w"))
