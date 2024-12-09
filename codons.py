def create_codon_dict(file_path):
    # Read rows from the file
    rows = read_file(file_path)

    # Initialize an empty dictionary
    codon_dict = {}

    # Process each row to populate the dictionary
    for row in rows:
        # Strip newline characters and split by tab
        parts = row.strip().split('\t')
        
        # Ensure the row has the expected number of parts
        if len(parts) >= 3:
            codon = parts[0]  # First column: codon
            amino_acid = parts[2]  # Third column: amino acid abbreviation
            
            # Update the dictionary
            codon_dict[codon] = amino_acid

    return codon_dict
