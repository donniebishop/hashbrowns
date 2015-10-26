import hashlib

def hash_maker(orig):
    ORIGINAL = orig
    MD5 = hashlib.md5(orig).hexdigest()
    SHA1 = hashlib.sha1(orig).hexdigest()
    SHA224 = hashlib.sha224(orig).hexdigest()
    SHA256 = hashlib.sha256(orig).hexdigest()
    SHA512 = hashlib.sha512(orig).hexdigest()

    hashes = {
        'original':ORIGINAL,
        'md5':MD5,
        'sha1':SHA1,
        'sha224':SHA224,
        'sha256':SHA256,
        'sha512':SHA512,
    }

    return hashes
