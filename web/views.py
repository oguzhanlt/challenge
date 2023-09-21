from django.shortcuts import render
from .vigenere import encrypt, decrypt
from django.http import JsonResponse


def index(request):
    if request.method == 'POST':
        plaintext = request.POST.get('plaintext')
        keyword = request.POST.get('keyword')
        action = request.POST.get('action')

        if action == 'encrypt':
            ciphertext = encrypt(plaintext, keyword)
        elif action == 'decrypt':
            ciphertext = decrypt(plaintext, keyword)
        else:
            ciphertext = ""

        return render(request, 'index.html', {'ciphertext': ciphertext})

    return render(request, 'index.html')

SECRET_SOLUTIONS = ["saarland University", "cispa", "cryptography", "informatics"]

def validate_word(request):
    word = request.POST.get('word', '').strip().lower()  # Convert user input to lowercase
    correct = word in (solution.lower() for solution in SECRET_SOLUTIONS)

    return JsonResponse({'correct': correct})
