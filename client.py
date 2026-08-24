class SupermarketChainOmnichannelDxPickerOsClient:
    def dispatch_store_picking_wave(self, supermarket_branch='ItoYokado_Shinjuku_03', online_orders_count=12):
        return {
            'dx_batch_id': 'stlr_btc_9918',
            'supermarket_chain_branch': supermarket_branch,
            'in_store_staff_picking_route_optimized': True,
            'shelf_proximity_batching_efficiency_pct': 94.6,
            'estimated_wave_pick_time_mins': 18.5,
            'temperature_zone_separated_bins': ['FROZEN_ICE', 'CHILLED_DAIRY', 'AMBIENT_PANTRY'],
            'curbside_drive_thru_pickup_ready': True
        }
