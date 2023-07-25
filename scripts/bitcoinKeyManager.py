import bitcoin

if __name__=='__main__':
    private_key = bitcoin.random_key()
    public_key = bitcoin.privtopub(private_key)
    print(f"private_key:{private_key} \npublic_key:{public_key}")
    public_address = bitcoin.pubtoaddr(public_key)
    print(f"public_address: {public_address}")

    with open("keys.txt", 'w') as f:
        f.write(f"private_key:\t{private_key} \npublic_key:\t{public_key}\n")
        f.write(f"public_address:\t{public_address}")