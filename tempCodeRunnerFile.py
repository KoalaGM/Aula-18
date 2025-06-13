    fig, ax = plt.subplots(1, 2, figsize=(18, 6))

    if not df_roubo_veiculo_outliers_inferiores.empty:
        dados_inferiores = df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True)

        ax[0].barh(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'])
    else:
        dados_inferiores = df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True).head(10)
        barras = ax[0].bar(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'], color='black')
        ax[0].bar_label(barras, label_type='edge', padding=3,fontsize=8)
        ax[0].tick_params(axis='x', rotation=75, labelsize=8)
        ax[0].set_title('Menores Roubos')
        # ax[0].set_xticks([])
        # ax[0].set_yticks([])


    if not df_roubo_veiculo_outliers_superiores.empty:
        dados_superiores = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=True)

        ax[1].barh(dados_superiores['munic'], dados_superiores['roubo_veiculo'])
    else:
        ax[1].text(0.5, 0.5, 'Sem Outliers', ha='center', va='center', fontsize=8)
        ax[1].set_title('Outliers Superiores')
