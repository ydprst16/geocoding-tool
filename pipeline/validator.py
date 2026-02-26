def validate_dataframe(df):
    if "alamat" not in df.columns:
        raise Exception("Kolom 'alamat' tidak ditemukan")

    if "kode_kec" not in df.columns:
        raise Exception("Kolom 'kode_kec' tidak ditemukan")

    for col in ["lat", "long", "status"]:
        if col not in df.columns:
            df[col] = ""

    return df