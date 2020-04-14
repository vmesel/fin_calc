

def calculate_movements_sum(df, movements_col):
    return df[movements_col].sum()


def calculate_periodic_contribution(df, patrimony_col, movements_col):
    df = df.copy()
    df["contribution"] = 100
    df["daily_pat_delta"] = (
        df[patrimony_col] - df[movements_col]) / \
        (df[patrimony_col].shift(1))
    
    df["daily_pat_delta"].iloc[0] = 1
    df["contribution"] = 100 * df["daily_pat_delta"].cumprod()

    return df


def calculate_return_based_on_index(df, contribution_col, start_index, end_index):
    df = df.copy()
    initial_contribution_value = df[contribution_col].iloc[start_index]
    final_contribution_value = df[contribution_col].iloc[end_index]

    return final_contribution_value / initial_contribution_value
