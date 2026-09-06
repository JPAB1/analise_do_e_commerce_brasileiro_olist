import pandas as pd

def limpar_e_preparar():
    print("Iniciando limpeza de dados...")
    
    # Carregar dados
    df_orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
    df_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
    df_customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
    
    # Cruzamento
    df = df_orders.merge(df_items, on="order_id").merge(df_customers, on="customer_id")
    
    # 1. Tratar valores ausentes
    # Preencher campos de texto vazios e descartar registros críticos sem data de entrega
    df['order_delivered_customer_date'] = df['order_delivered_customer_date'].fillna(df['order_estimated_delivery_date'])
    
    # 2. Padronizar formatos de dados
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['customer_state'] = df['customer_state'].str.upper()
    df['customer_city'] = df['customer_city'].str.title()
    
    # 3. Criar Nova Coluna Derivada 1: Valor Total Pago (Preço + Frete)
    df['valor_total_pedido'] = df['price'] + df['freight_value']
    
    # 4. Criar Nova Coluna Derivada 2: Tempo de Entrega Real (em Dias)
    df['dias_para_entrega'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
    
    # Tratar inconsistências de datas negativas (entrega antes da compra por erro de sistema)
    df = df[df['dias_para_entrega'] >= 0]
    
    # Salvar a base limpa pronta para visualização
    df.to_csv("data/processed/vendas_consolidadas_brasil.csv", index=False)
    print("Processamento concluído! Arquivo gerado em: data/processed/vendas_consolidadas_brasil.csv")

if __name__ == "__main__":
    limpar_e_preparar()
