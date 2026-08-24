from client import SupermarketChainOmnichannelDxPickerOsClient

def main():
    client = SupermarketChainOmnichannelDxPickerOsClient()
    res = client.dispatch_store_picking_wave('Life_Supermarket_Shibuya', 16)
    print('DX Wave: ' + res['dx_batch_id'] + ' at ' + res['supermarket_chain_branch'])
    print('Shelf Batching Efficiency: ' + str(res['shelf_proximity_batching_efficiency_pct']) + '% | Est Pick Time: ' + str(res['estimated_wave_pick_time_mins']) + ' mins')
    print('Temperature Zones: ' + ', '.join(res['temperature_zone_separated_bins']))

if __name__ == '__main__':
    main()
