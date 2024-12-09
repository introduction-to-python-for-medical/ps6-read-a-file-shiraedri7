def create_codon_dict(file_path):

    codons_dict = {}
    
    # Open and read the file
    file = open(file_path, 'r')
    rows = file.readlines()
    file.close()

    # Process each row to populate the dictionary
    for row in rows:
        # Strip newline characters and split by tab
        parts = row.strip().split('\t')
        
        if len(parts) >= 3:  # Ensure the row has the expected number of parts
            codon = parts[0]  # First column: codon
            amino_acid = parts[2]  # Third column: amino acid abbreviation
            
            # Update the dictionary
            codons_dict[codon] = amino_acid

    return codons_dict
