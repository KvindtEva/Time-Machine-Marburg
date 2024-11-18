def strings_to_links(df, columns):

    for i in df.index:
        for column in columns:
            if df.loc[i, column] != '[]':
                df.at[i, column] =  df.loc[i, column][2:-2].split('\', \'')
            else:
                df.at[i, column] = []