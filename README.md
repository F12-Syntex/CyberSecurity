# Cryptography Assignment: Tess of the d'Urbervilles

This repository contains the solutions for the Cryptography Assignment based on Thomas Hardy's novel "Tess of the d'Urbervilles". The assignment consists of seven exercises, each involving decrypting an extract from the novel using different ciphers.

## Assignment Objectives

The objectives of this assignment are:
- To gain practical experience with encryption, decryption, plaintext, ciphertext, and keys.
- To understand the impact of having certain quantities of ciphertext available.
- To learn basic cryptology techniques such as substitution, permutation, and frequency analysis.
- To develop problem-solving skills by devising solutions to decrypt the given ciphertexts.

## Exercises

1. **Exercise 1** (2 marks): Decrypt an extract encoded with a Caesar cipher.
2. **Exercise 2** (3 marks): Decrypt an extract encoded with a Vigenere cipher using the 21-letter key "TESSOFTHEDURBERVILLES".
3. **Exercise 3** (4 marks): Decrypt an extract encoded with a Vigenere cipher using an arbitrary sequence of six letters as the key.
4. **Exercise 4** (5 marks): Decrypt an extract encoded with a Vigenere cipher using an arbitrary sequence of between 4 and 6 letters as the key.
5. **Exercise 5** (5 marks): Decrypt an extract encoded with a transposition cipher, where the plaintext is written row-wise across a certain number of columns (between 4 and 6).
6. **Exercise 6** (5 marks): Decrypt an extract encoded with a transposition cipher, where the plaintext is written row-wise across six columns, and the ciphertext is formed by reading out successive columns in an arbitrary order.
7. **Exercise 7** (6 marks): Decrypt an extract encoded with a general substitution cipher, using a randomly chosen mapping from the 27-character alphabet onto itself.

## Files

- `tess.txt`: The ASCII text of "Tess of the d'Urbervilles" from Project Gutenberg.
- `tess27.txt`: A reduced version of `tess.txt` using a 27-character alphabet.
- `tess26.txt`: A further reduced version of `tess27.txt` using a 26-character alphabet.
- `exercise1.txt` to `exercise7.txt`: Text files containing the solutions for each exercise, including the first 30 characters of the decrypted plaintext and a description of the decryption approach.

## Submission

The solutions for each exercise should be submitted as text files named `exercise1.txt` to `exercise7.txt` in the designated folder on the Raptor server. The format of each file should be as follows:
- Line 1: The first 30 characters of the decrypted plaintext.
- Line 2: Blank line.
- Line 3 onwards: A description of the decryption approach and any tools or programs used.

## Note

The provided files `tess26.txt` and `tess27.txt` are intended for checking answers and analyzing language statistics, not for assisting in the decryption process.

Please refer to the assignment specification for more details on the rules, restrictions, and submission guidelines.