_base_ = '../retinanet/retinanet_r50_fpn_coco.py'
model = dict(
    bbox_head=dict(
        loss_cls=dict(
            _delete_=True,  # 防止合并字典时候错误，设置为True会忽略base相关配置
            type='GHMC',
            bins=30,  # 将g纵坐标均匀切分为bin个长度,论文中的M
            momentum=0.75,
            use_sigmoid=True,
            loss_weight=1.0),
        loss_bbox=dict(
            _delete_=True,
            type='GHMR',
            mu=0.02,
            bins=10,
            momentum=0.7,
            loss_weight=10.0)))
optimizer_config = dict(
    _delete_=True, grad_clip=dict(max_norm=35, norm_type=2))
