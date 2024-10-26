
def strings_to_links(df, columns):

    for i in range(df.shape[0]):
        for column in columns:
            _ = df.iloc[i][column]
            if _ == '[]':
                df.at[i, column] = []
            else:
                df.at[i, column] =  _[2:-2].split('\', \'')
