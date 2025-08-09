import os

from src.logger import logging
from src.configuration import ConfigurationManager

import transformers
from transformers import TrainingArguments, Trainer, DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch

class ModelTrainer:
    def __init__(self, config):
        self.config = config
    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logging.info(f"Using device: {device}")

        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)

        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=1,                 
            warmup_steps=500,
            per_device_train_batch_size=1,
            per_device_eval_batch_size=1,
            weight_decay=0.01,
            logging_steps=10,                    
            save_steps=500,          
            save_total_limit=2,                      
            gradient_accumulation_steps=1
        )

        trainer = Trainer(
            model=model_pegasus, args=trainer_args, tokenizer=tokenizer, data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"], eval_dataset=dataset_samsum_pt["validation"]
        )

        trainer.train()

        logging.info("Model training completed")

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus_samsum_model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
        logging.info("Model and tokenizer saved successfully")
