from transformers import pipeline
clasficador = pipeline("sentiment-analysis")
print(clasficador("Me encanta programar en Python!"))
print(clasficador("No me gusta el clima hoy."))