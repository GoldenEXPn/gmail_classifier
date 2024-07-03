<p align="center">
  <img width="100"alt="Logo(Change Later)"src="https://raw.githubusercontent.com/nicejade/arya-jarvis/master/assets/images/logo.png">
</p>

<h1 align="center">Gmail Classifier</h1>

<div align="center">
  <strong>
    This is an ongoing project aiming to classify user emails into categories and provide a priority rank for each email message.
  </strong>
</div>

<br>

<div align="center">
  <a href="https://github.com/GoldenEXPn/gmail_classifier?tab=MIT-1-ov-file"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT License"></a>
  <a href="https://prettier.io/"><img src="https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat" alt="Prettier"></a>
</div>

## Goal and Philosophy

Workers, professors, and students are always overwhelmed by abundant email messages. Plenty of spam emails or subscription emails from apps can easily make people miss important work messages. Inspired by this, we decided to pretrain a classification model and create a web app based on it to help people easily find work email messages. In the near future, the web app can even automatically categorize and set priorities for each email message!


## Website UI elements  
<a href="https://www.figma.com/design/TvctykmBki1zY0chNWPaaa/WebUI_draft?node-id=0-1&t=yuBynKHzwnRUtpTY-1"> figma </a>


## Resources: 
<a href="https://www.figma.com/design/TvctykmBki1zY0chNWPaaa/WebUI_draft?node-id=0-1&t=yuBynKHzwnRUtpTY-1"> figma </a>


## Dataset:

We leverage <a href="https://www.cs.cmu.edu/~enron/"> Enron Email Dataset </a> in fine-tuning. The dataset contains around 500K email messages, and we filter all empty-title, RE and FW messages and select around 5K high-quality email messages.
